class BatchMonitor:

    def __init__(self, application_exec, ps=None, task=None):
        self.application_exec = application_exec
        self.ps = ps
        self.task = task
