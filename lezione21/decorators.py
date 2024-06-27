
# """def parent():

#     print("sono in parent")
    
#     def first_child():

#         print("sono in first child")

#     def second_child():

#         print("sono in second child")
    
#     second_child()
#     first_child()
    
#     return second_child

# out_function = parent()
# print(out_function)"""
# import random
# import time

# def get_time(func):
     
#     def wrapper(*args):

#         start = time.time()

#         func(*args)

#         end = time.time()
#         elapsed_time = end - start
#         print(f"{elapsed_time}")

#     return wrapper

# @get_time
# def say_hello(name : str)->None:
#     print(f"Hello {name}")


# say_hello("MARCO")

# @get_time
# def say_ciao(name : str)-> None:
#     print(f"Ciao {name}")




# say_ciao("Andrea")

# @get_time
# def random_list(upper_bound: int):

#     sleep_time: int = random.randint(0, upper_bound)
#     time.sleep(sleep_time)

# random_list(10)




# """def saluta(func):
#     func("Flavio")"""

# """saluta(say_hello)
# saluta(say_ciao)"""


# #GENERATORE
# def generatore():

#     yield "A"
#     yield "B"
#     yield "C"

# prova_generatore = generatore()
# print(next(prova_generatore))
# print(next(prova_generatore))


def funzione(id : int):
    import time
    import random
    sleep_time : int = random.randint(1,10)
    print(f"id={id} time {time.time()}")
    time.sleep(sleep_time)
    print(f"id={id} time {time.time()}")
    

if __name__ == "__main__":

    import threading
    

    list_threading : list [threading.Thread]= []

    # for id in range(3):

    #     x: threading.Thread = threading.Thread(target=funzione, args=(id,))
    #     list_threading.append(x)
    #     print(f"prima di runnare il thread {time.time()}")
    #     x.start()
    #     x.join()         #aspetta che il processo termini
    #     print(f"Ho runnato il thread {time.time()}")

    # for t in list_threading:

    #     t.join()
    #     print(f"Terminato") tutto il for lo posso scriver con with concorrent

    from concurrent.futures import ThreadPoolExecutor

    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(funzione, range(10))