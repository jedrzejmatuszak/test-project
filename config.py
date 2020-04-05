from .mx_objects import BatchMonitor


class Config:

    def __init__(self, murex, env):
        self.murex = murex
        self.env = env
        self.batch_moniotr = None
        self.jcl = None

    def add_batch_monitor(self, application_exec):
        obj = BatchMonitor(application_exec)
        self.batch_moniotr = obj
