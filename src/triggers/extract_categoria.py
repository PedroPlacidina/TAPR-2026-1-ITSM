import logging
import os
import azure.functions as func
import pyodbc

bp = func.Blueprint()

@bp.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False) 
def extract_categoria(myTimer: func.TimerRequest) -> None:
    logging.info('Iniciando sincronização: itsm.categoria')

    
    conn_str_source = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={os.getenv('SQL_SERVER_SOURCE')};"
        f"DATABASE={os.getenv('SQL_DATABASE_SOURCE')};"
        f"UID={os.getenv('SQL_USER_SOURCE')};"
        f"PWD={os.getenv('SQL_PASSWORD_SOURCE')};"
        "Encrypt=yes;TrustServerCertificate=no;"
    )

    conn_str_target = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={os.getenv('SQL_SERVER_TARGET')};"
        f"DATABASE={os.getenv('SQL_DATABASE_TARGET')};"
        f"UID={os.getenv('SQL_USER_TARGET')};"
        f"PWD={os.getenv('SQL_PASSWORD_TARGET')};"
        "Encrypt=yes;TrustServerCertificate=no;"
    )

    try:
       
        with pyodbc.connect(conn_str_source) as src_conn:
            cursor_src = src_conn.cursor()
            cursor_src.execute("SELECT id_categoria, cd_categoria, nm_categoria, ds_descricao, fl_ativo FROM itsm.categoria")
            rows = cursor_src.fetchall()

        if rows:
            with pyodbc.connect(conn_str_target) as tgt_conn:
                cursor_tgt = tgt_conn.cursor()
                
                cursor_tgt.execute("SET IDENTITY_INSERT itsm.categoria ON")

                cursor_tgt.execute("DELETE FROM itsm.categoria") # Limpa a tabela antes de carregar
                
                insert_sql = "INSERT INTO itsm.categoria (id_categoria, cd_categoria, nm_categoria, ds_descricao, fl_ativo) VALUES (?, ?, ?, ?, ?)"
                
                for row in rows:
                    cursor_tgt.execute(insert_sql, (row.id_categoria, row.cd_categoria, row.nm_categoria, row.ds_descricao, row.fl_ativo))
                
                cursor_tgt.execute("SET IDENTITY_INSERT itsm.categoria OFF")
                tgt_conn.commit()
                
                logging.info(f"Sucesso! {len(rows)} registros carregados na tabela categoria.")

    except Exception as e:
        logging.error(f"Erro ao processar categoria: {str(e)}")