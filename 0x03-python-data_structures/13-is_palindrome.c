#include <stdio.h>
#include <stdlib.h>

typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

int is_palindrome(listint_t **head)
{
    listint_t *temp = *head;
    int stack[2048];
    int top = 0;
    int i;

    if (head == NULL || *head == NULL)
        return (1);

    while (temp != NULL)
    {
        stack[top++] = temp->n;
        temp = temp->next;
    }

    for (i = 0; i < (top / 2); i++)
    {
        if (stack[i] != stack[top - i - 1])
            return (0);
    }

    return (1);
}
