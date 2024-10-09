import concurrent.futures

#* NO.3 
#* 一个用线程池来管理并发任务的模版

string = "你好吗？我很好" #出自岩井俊二的《情书》

def yours_task(character):#*你希望并发执行的任务
    print(character, end='')

def submittask(executor,futures):
    for _ in string :
        #*concurrent.futures.Executor线程池执行器，使用该执行器提交你的任务
        #*submit()提交任务，返回结果的顺序不可控，如果希望返回的结果是有序执行的话，可以用map()
        future = executor.submit(yours_task,string[_])
        future = executor.map(yours_task,string[_])
    futures.append(future)

def thread_pool():
    futures = []
    #*使用线程池，无需关心线程的创建与销毁，只负责任务的提交，不负责任务的分发
    with concurrent.futures.Executor as executor:
        submittask(executor,futures)
        for future in concurrent.futures.as_completed(futures):#as_completed需要接受一个迭代器
            try:
                future.result()
            except Exception as e:
                print(f"线程的错误：{e}")

if __name__ == '__main__':
    thread_pool()