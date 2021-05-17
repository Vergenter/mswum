import time

'''
Aby używać timera wystarczy zaimportować go do notebooka:
    from Timer import *
Zdefiniować obiekt
    t = Timer()
A następnie w odpowiednim miejscu wystartować 
    t.start()
Oraz zatrzymać
    t.stop()
stop() od razu poda ilość czasu spędzonego przy wykonaniu kodu.

* Timer liczy czas procesora.

Do liczenia czasu można również wykorzystac magiczną funkcję %time.

Alternatywnie można używać wbudowanych magiczych metod np.:
    %%timeit ... - zlicz czas dla całego bloku kodu (sprawdź czy "blok" obejmuje cały kod. Najlepiej żeby znajdował się w funkcjach/metodach)
    %timeit operacja - zlicz czas dla wybranej jednej operacji (przydantne przy funkcjach np. %timeit getData())
Timeit dla małych/krótkich operacji wykona kilka pętli i wyciągnie z nich średnią.
Aby dowiedzieć się więcej o magicznej funkcji %timeit w bloku notebooka nalezy wpisać:
    %timeit?

* Wyniki z timeit i Timera są do siebie zbliżone

Do pomiaru pamięci można doinstalować paczkę memory_profiler
    pip install memory_profiler
Trzeba ją załadować w notebooku przed pomiarem
    %load_ext memory_profiler
Pomiar pamięci odbywa się za pomocą %memit dodawanym przed opracją do pomiaru dlatego najlepiej aby operacje były w pętli, np.
    %memit sum_of_lists(1000000)
Tak jak w timeit, istnieje alternatywa dla bloków: %%memit
Memit liczy pamięć używaną przez notebook, więc bardziej interesuje nas zmiana pamięci.
Aby poprawnie wykonać pomiar pamięci wypadałoby najpierw zapisać opearcje z osobnym pliku .py, a następnie uruchomić profilowanie 
z pliku, np.:
    from nazwa_pliku import nazwa_funkcji
    %mprun -f nazwa_funkcji nazwa_funkcji(...)
%mprun zwróci informacje o zużyciu pamięci dla każdego wiersza w pliku.
Aby dowiedzieć się więcej o magicznej funkcji %memit w bloku notebooka nalezy wpisać:
    %memit?

*** UWAGA ***
Staramy się nie używać %memit w połaczeniu z %timeit - timeit policzy czas memit, a memit policzy pamięc z timeit.

'''

class Timer:
    def __init__(self):
        self.time = 0
        self.start_time = None

    def start(self):
        if self.start_time is not None:
            raise Exception("Timer is running. Use stop() to stop it.")

        self.start_time = time.perf_counter()
    
    def stop(self):
        if self.start_time is None:
            raise Exception("Timer is not running. Use start() to start it.")
        
        stop = time.perf_counter()
        self.time = stop - self.start_time
        self.start_time = None
        self.print()

    def print(self):
        print(f"Elapsed time: {self.time:0.4f} seconds.")