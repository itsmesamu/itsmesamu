class job:
    id = 0
    def __init__(self, zeitaufwand, dringlichkeit):
        self.id = job.id
        job.id += 1
        self.zeitaufwand = zeitaufwand
        self.dringlichkeit = dringlichkeit

    def __repr__(self):
        return str(self.id)

j1 = job(3, 2)
j2 = job(4, 1)
j3 = job(5, 3)

class Scheduler:
    def schedule(self, jobs: list):
        def job_zu_dringlichkeit(job: job):
            return job.dringlichkeit
        erg = sorted(jobs, key=job_zu_dringlichkeit)
        return erg

s = Scheduler()
print(s.schedule([j1,j2,j3]))