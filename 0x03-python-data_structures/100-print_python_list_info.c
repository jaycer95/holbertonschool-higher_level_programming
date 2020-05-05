B#include <object.h>
#include <Python.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = Py_Size(p);
	int i;
	PyListObject *o = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", o->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(o->PyList_GetITEM(o, i))->tp_name);
}
