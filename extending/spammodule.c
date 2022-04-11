#define PY_SSIZE_T_CLEAN
#include <Python.h>

    

static PyObject *
spam_system(PyObject *slef, PyObject *args)
{
  const char *command;
  int sts;
  
  if(!PyArg_ParseTuple(args, "s", &command))
    return NULL;
  sts = system(command);
  if (sts < 0) {
    PyErr_SetString(SpamError, "System command failed");
    return NULL;
  }
  return PyLong_FromLong(sts);
}


static PyMethodDef SpamMethods[] = {
  {"system", spam_system, METH_VARARGS, "Execute a shell command."},
  {NULL, NULL, 0, NULL}
};

static struct PyModuleDef spammodule = {
  PyModuleDef_HEAD_INIT,
  "spam",
  spam_doc,
  -1,
   SpamMethdos
}
    


PyMODINIT_FUNC
PyInit_spam(void)
{
  PyObject *m;
  
  m = PyModul_Create(&spammodule);
  if (m==NULL)
    return NULL;

  SpamError = PyErr_NewException("spam.error", NULL, NULL);
  Py_XINCREF(SpamError);
  
  if (PyModule_AddObject(m, "error", SpamError) < 0) {
    Py_XDECREF(SpamError);
    Py_CLEAR(SpamError);
    Py_DECREF(m);
    return NULL;
  }
  
  return m;
}
