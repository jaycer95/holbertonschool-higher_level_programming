#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/**
 *
 *
 *
 */
int is_palindrome(listint_t **head)
{
	listint_t *adv = *head;
	int len = 0, i = 0;
	char *s;

	if (!adv || !adv->next)
		return(1);
	while(adv)
	{
		adv = adv->next;
		len++;
	}
	adv = *head;
	s = malloc(sizeof(len));
	while(adv)
	{
		s[i] = adv->n;
		adv = adv->next;
		i++;
	}
	i = 0;
	for(; i < len / 2; i++)
	{
		if (s[i] != s[len - i - 1])
			    return (0);
	}
	return(1);
}
