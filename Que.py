import random

class PrintQue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


class Job:

    def __init__(self):
        self.pages = random.randint(1, 11)

    def print_page(self):
        if self.pages > 0:
            print(self.pages)
            self.pages -= 1

    def check_complete(self):
        if self.pages == 0:
            return True
        return False


class Printer:

    def __init__(self):
        self.current = None

    def get_job(self, print_queue):
        try:
            self.current = print_queue.dequeue()
        except IndexError:
            return "Nothing else to print!"

    def print_job(self, job):
        while job.pages > 0:
            job.print_page()

        if job.check_complete():
            return "Complete!"
        else:
            return "ERROR."


if __name__ == "__main__":

    job = Job()
    printer = Printer()
    print_q = PrintQue()

    print(job.print_page())
    print(job.check_complete())

    print_q.enqueue(job)
    print(print_q.items)

    printer.get_job(print_q)
    print(print_q.items)
    print(printer.print_job(printer.current))









