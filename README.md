# async_practice


https://www.youtube.com/watch?v=iG6fr81xHKA


https://github.com/santiagobasulto/pycon-concurrency-tutorial-2020

> https://www.youtube.com/watch?v=18B1pznaU1o&t=7455s
> 
> https://www.youtube.com/watch?v=bs9tlDFWWdQ
> 
> https://brownbears.tistory.com/540
> 

https://soooprmx.com/python-asycnio-%EC%97%90%EC%84%9C-%EB%9F%B0%EB%A3%A8%ED%94%84%EB%A5%BC-%EA%B8%B0%EB%B0%98%EC%9C%BC%EB%A1%9C-non-blocking-%EC%BD%94%EB%93%9C-%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B0/?amp
# 핵심
- await가 등장하면 다른 코루틴으로 제어권이 넘어간다. 다음의 예제는 여러 코루틴을 한꺼번에 스케줄링하고 as_completed를 이용해서 하나씩 그 결과를 얻어 처리하는 가장 기본적인 패턴이다.
- await를 만났으니 여기서 일시정지하고 스케줄링된 다음 코루틴으로 넘어간다.
- print() 함수는 단일 스레드 내에서는 블럭킹함수이기 때문에 한 작업이 출력하는 중에는 다른 작업이 동시에 출력할 수 없다.



https://soooprmx.com/asyncio/
# 핵심_1
> 일단 결론부터 말하자면 코루틴, Task, Future 객체는 모두 Awaitable(대기가능) 객체이다. 대기 가능 객체는 await 다음에 올 수 있는 것으로 이해하면 된다. 이들은 실행흐름이 주 루틴과 선형으로 연결되지 않지만, 최종적으로 결과가 필요한 시점에 await와 결합하여 실행의 종료를 기다리게 된다.
# 핵심_2
> 코루틴은 간단히 asyncio.create_task() (Python 3.6 이전은 asyncio.ensure_future()) 함수를 사용해서 Task로 만들 수 있다. Task로 만들어지는 과정에서 코루틴은 런루프에 등록되어 스케줄링되고, (언젠지는 모르지만) 실행 가능한 시점이 오면 실행을 시작할 수 있다.
### - Future
> 싱글스레드의 비동기 IO나 멀티스레드/멀티 프로세스 패러다임에서 중요한 것은 비동기 실행이고, 비동기 실행의 특징은 실제 처리 완료와 상관없이 디스패치를 담당하는 함수는 바로 리턴하는 non-blocking 함수라는 점이다.
>
> 
