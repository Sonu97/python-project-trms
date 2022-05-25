def _result(result):
    if result:
        return ApprovalsImplRepo(approval_id=result[0], reim_form_id=result[1], supervisor_approved_date=result[2],
                                 supervisor_denied_reason=result[3], dept_head_approved_date=result[4],
                                 benco_approved_date=result[5])
    else:
        None


class ApprovalsImplRepo:
    pass
