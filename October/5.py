class Employee():
    def __init__(self, job):
        self.job = job
    def work(self, job):
        print(job)
        
class Engineer(Employee):
    def work(self):
        print('Engineer')
        
def main():
    job = input('job: ')
    jobtype = Employee(job)
    jobtype.work(job)
    engineerjob = Engineer(job)
    engineerjob.work()
       
main()
