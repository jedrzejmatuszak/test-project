from mx_objects import BatchMonitor


class Config:

    def __init__(self, murex, env):
        self.murex = murex
        self.env = env
        self.batch_monitor = None
        self.jcl = None

    def add_batch_monitor(self, application_exec):
        if '=' in application_exec:
            obj = BatchMonitor._create_batch_monitor(application_exec)
        else:
            obj = BatchMonitor(application_exec)
        self.batch_monitor = obj


command = {
    'BM_TASK1_NEW': '/murex/uimx/bin/ProcessingScript.sh G=FO U=MXEODUSER N=DUPAJASIA',
    'BM_TASK2_OLD': '/murex/uimx/bin/ProcessinsScript.sh BM:TASK2_DUPA SYSMO_ALL MUREX.NO_FLEX',
    'BM_TASK3_OLD': '/bin/ProcessingScript.sh BM:TASK3_DUPA IF_FUN_GL MUREX_NO_FLEX',
    'BM_TASK4_NEW': '/env/bin/PS.sh script G=BO D=FO_AT N=MUREXEODUSER'
}