#include "lists.h"

/**
 * check_cycle - if a linked list contain a cycle will be checked
 * @list: the aprameter to be check which list
 * Return: 1 or 0 where positive means has where negative means not
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;

	if (!list)
		return (0);
	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}
	return (0);
}
