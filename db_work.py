from typing import Tuple, List
from db_context_manager import DBContextManager


def select(db_config: dict, sql: str) -> Tuple[Tuple, List[str]]:
    result = tuple()
    schema = []
    with DBContextManager(db_config) as cursor:
        if cursor is None:
            raise ValueError('Курсор не создан')
        cursor.execute(sql)
        schema = [column[0] for column in cursor.description]
        result = cursor.fetchall()
    return result, schema


def select_dict(dbconfig: dict, _sql: str):
    with DBContextManager(dbconfig) as cursor:
        if cursor is None:
            raise ValueError('Курсор не создан')
        cursor.execute(_sql)
        result = []
        schema = [column[0] for column in cursor.description]
        for row in cursor.fetchall():
            result.append(dict(zip(schema, row)))
    return result


def call_proc(dbconfig: dict, proc_name: str, *args):
    with DBContextManager(dbconfig) as cursor:
        if cursor is None:
            raise ValueError('Курсор не создан')
        param_list = []
        for arg in args:
            param_list.append(arg)
        res = cursor.callproc(proc_name, param_list)
    return res


def insert(dbconfig: dict, _sql: str):
    with DBContextManager(dbconfig) as cursor:
        if cursor is None:
            raise ValueError('Курсор не создан')
        result = cursor.execute(_sql)
    return result
