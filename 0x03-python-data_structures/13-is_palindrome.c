#include "lists.h"
/**
 * check_palin - check if a linked list is plaindrome
 * @h: of the link list
 * @next: next pointer to head
 * Return: pointer
 */
bool check_palin(listint_t **h, listint_t *next)
{
	listint_t *current = NULL;
	bool palin = true;

	if (next != NULL)
	{
		current = next;
		next = current->next;
		palin = check_palin(h, next);
	}
	if (current == NULL)
		return true;
	if (palin)
	{
		if ((*h)->n != current->n)
		{
			palin = false;
			return (palin);
		}
		else
		{
			*h = (*h)->next;
			palin = true;
			return (palin);
		}
	}
	else
		return (false);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *next;

	if (current == NULL)
		return (1);
	if (current->next != NULL)
		next = current->next;
	else
		return (1);
	if (check_palin(head, next))
		return (1);
	else
		return (0);
}
