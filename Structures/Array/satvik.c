#include <stdio.h>

int i,n;

int main()
{
    int max;

    scanf("%d", &max);

    int a[max];

    scanf("%d", &n);// number of elements to be inserted
    for ( i = 0; i < n; i++)
    {
        scanf("%d", &a[i]); // elements defined
    }

    int target;

    scanf("%d", &target);

    int x; // element to be inserted

    scanf("%d", &x);

    int position = -1;

    int len = 0;

    for ( i = 0; i < n; i++)
    {
        if (a[i] == target)
        {
            position = i;
            break;
        }
        
    }
    if (position == -1)
    {
        printf("Target Element Not Found\n");

        for ( i = 0; i < n; i++)
        {
            printf("%d ", a[i]);
        }
        
    }
    else
    {
        len = n+1;
        for ( i = n; i > position; i--)
        {
            a[i] = a[i-1]; // shifts elements forward
        }
        printf("testing");
        for ( i = 0; i < len; i++)
        {
            printf("%d ", a[i]);
        }
        printf("\n");
        // int x; // element to be inserted
        // scanf("%d", &x);
        a[position + 1] = x;
        for ( i = 0; i < n+1; i++)
        {
            printf("%d ", a[i]);
        }
        
    }
    
    
    return 0;
    

}