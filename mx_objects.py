import re


class BatchMonitor:

    re_new_ps = re.compile('(?<=PS=)[\S]+', flags=re.ASCII)
    re_old_ps = re.compile('(?<=ProcessingScript[.]sh)[\S]+', flags=re.ASCII)
    re_mxgroup = re.compile('(?<=G=)[\S]+', flags=re.ASCII)
    re_new_nickname = re.compile('(?<=N=)[\S]+', flags=re.ASCII)
    re_old_nickname = re.compile('(?<=MXPR)[\S]+', flags=re.ASCII)
    re_desk = re.compile('(?<=D=)[\S]+', flags=re.ASCII)
    re_user = re.compile('(?<=U=)[\S]+', flags=re.ASCII)

    def __init__(self, application_exec):
        self.application_exec = application_exec
        self.ps = re.match(self.re_old_ps, application_exec).group()
        self.nickname = re.match(self.re_old_nickname, application_exec).group()

    @classmethod
    def _create_batch_monitor(cls, application_exec):
        cls.application_exec = application_exec
        cls.ps, cls.mxgroup, cls.nickname, cls.desk, cls.user = cls._get_application_execution_params(application_exec)
        return cls

    @classmethod
    def _get_application_execution_params(cls, application_exec):
        ps = re.match(cls.re_new_ps, application_exec).group() if re.match(cls.re_new_ps, application_exec) is not None else None
        mxgroup = re.match(cls.re_mxgroup, application_exec).group() if re.match(cls.re_mxgroup, application_exec) is not None else None
        nickname = re.match(cls.re_new_nickname, application_exec).group() if re.match(cls.re_new_nickname, application_exec) is not None else None
        desk = re.match(cls.re_desk, application_exec).group() if re.match(cls.re_desk, application_exec) is not None else None
        user = re.match(cls.re_user, application_exec).group() if re.match(cls.re_user, application_exec) is not None else None
        return ps, mxgroup, nickname, desk, user
