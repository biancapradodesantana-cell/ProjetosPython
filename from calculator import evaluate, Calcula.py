from calculator import evaluate, CalculatorError, History

MEMORY_KEY = "M"

def print_help():
    print("""
Comandos disponíveis:
  <expressão>        Calcula uma expressão. Ex: 2 * (3 + sqrt(16))
  ans                 Usa o último resultado em uma nova expressão
  M+ <expr>           Soma o resultado da expressão à memória
  M- <expr>           Subtrai o resultado da expressão da memória
  MR                  Mostra o valor atual da memória
  MC                  Limpa a memória
  hist                Mostra o histórico de cálculos da sessão
  salvar <arquivo>    Salva o histórico em um arquivo de texto
  carregar <arquivo>  Exibe um histórico salvo anteriormente
  limpar              Limpa o histórico da sessão
  ajuda               Mostra esta mensagem
  sair                Encerra o programa
 
Funções: sqrt, sin, cos, tan, asin, acos, atan, log, ln, log2, exp,
         fact, abs, floor, ceil, radians, degrees
Constantes: pi, e, tau
""")

def build_variables(memory; float, last_result):
    variables = {MEMORY_KEY; memory}
    if last_result is no None:
        variables["ans"] = last_result
    return variables

 def main():
    print ("| Calculadora Cientifica |")
    print ("Digite 'Ajuda para ver os comandos disponiveis s.\n")
    history = History()
    memory = 0.0

    while True:
        try:
            raw = input(">> ").strip()
        except (E0FError, KeyboardInterrupt):
            print("\nAté a proxima!")
        break

        if not raw:
            continue

        lower = raw.lower()

        if lower in ("sair", "exit", "quit"):
            print("\nAté a proxima!")
            break
        
        if lower in ("ajuda", "help"):
            print_help()
            continue

        if  lower == "historico":
            entries = history.all
            if not entries:
                print ("[Histórico vazio]")
            for entry in entries:
                print(entry)
            continue
        
        if lower == "limpar":
            hitory.clear()
            print ("Histórico  limpo!")
            continue
        
        if lower.startswith("Salvar "):
            filename = raw.split (" ", 1)[1].strip()
            try:
                history.save (filename)
                print (f"Historico salvo em '{filename}'.")
            except 0SError as exc:
                print(f"Erro ao salvar: exc")
            continue

        if lower.startswith("carregar "):
            


        

   