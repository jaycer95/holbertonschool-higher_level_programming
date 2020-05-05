#include <Python.h>
/**
 * print_python_list_info - prints python list info
 * @p: pyobject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size;
	int i;
	PyListObject *o = (PyListObject *)p;
	PyObject *t;
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", o->allocated);
	for (i = 0; i < size; i++)
	{
		t = PyList_GetItem(p, i);
		printf("Element %i: %s\n", i, Py_TYPE(t)->tp_name);
	}
}
