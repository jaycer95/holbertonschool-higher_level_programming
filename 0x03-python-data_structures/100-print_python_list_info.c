#include <object.h>
#include <Python.h>
#include <listobject.h>
/**
 * print_python_list_info - prints python list info
 * @p: pyobject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = Py_Size(p);
	int i;
	PyListObject *o = (PyListObject *)p;
	Pyobject *t;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", o->allocated);
	for (i = 0; i < size; i++)
	{
		t = PyList_GetITEM(o, i);
		printf("Element %i: %s\n", i, Py_TYPE(t)->tp_name);
	}
}
