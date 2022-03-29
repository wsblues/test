// mylib.c
#include "Python.h"
#include <stdio.h>
 
static PyObject *ErrorObject;
 
// ���� �����ϴ� �Լ�
static PyObject* write_log(PyObject *self, PyObject *args) // ���ڴ� �̿Ͱ��� �����ȴ�.
{
    char* msg;
    FILE *fp;
    
    if(!PyArg_ParseTuple(args, "s", &msg))
        return NULL;
    
    fp = fopen("c:\\pylog.txt", "wt+");
    fprintf(fp, msg);
    fclose(fp);
    
    return Py_BuildValue("i", 0);    
}
 
/* methods ����ü �迭�� �����Ǵ� ������ {"��������� �޽���", �޽��� �����ϴ� ���� �����ϴ� �Լ���, ���� ����} */
static struct PyMethodDef methods[] =
{
    {"wlog", write_log, METH_VARARGS},
    {NULL, NULL}
};
 
//
void initmylib()
{
    PyObject* m;
   
   // Py_InitModule("����", �̸�⿡ ����� �޽����� ���� ����ü�迭 ������)
    m = Py_InitModule("mylib", methods);

    ErrorObject = Py_BuildValue("s", "error");
}