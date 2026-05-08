import logging
import azure.functions as func

app = func.FunctionApp()

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_analista(myTimer: func.TimerRequest) -> None:
        logging.info('Tabela analista')

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_categoria(myTimer: func.TimerRequest) -> None:
        logging.info('Tabela categoria')

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_chamado(myTimer: func.TimerRequest) -> None:
        logging.info('Tabela Chamado')

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_chamadosla(myTimer: func.TimerRequest) -> None:
        logging.info('Tabela chamado sla')

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_statushistorico(myTimer: func.TimerRequest) -> None:
        logging.info('Tabela chamado status historico')

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_cliente(myTimer: func.TimerRequest) -> None:
        logging.info('Tabela cliente organizacao')

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_csat(myTimer: func.TimerRequest) -> None:
        logging.info('Tabela csat avaliacao')

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_fila(myTimer: func.TimerRequest) -> None:
        logging.info('Tabela fila')

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_sla(myTimer: func.TimerRequest) -> None:
        logging.info('Tabela sla')

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_solicitante(myTimer: func.TimerRequest) -> None:
        logging.info('Tabela solicitante')
