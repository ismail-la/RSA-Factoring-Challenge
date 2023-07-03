#include <stdio.h>

int main()
{
long long int num = 239809320265259;
long int fact1 = 2;
long int fact2;

while (num % fact1)
{
if (fact1 <= num)
{
fact1++;
}
else
{
return (-1);
}

}


fact2 = num / fact1;
printf("%lld = %ld * %ld\n", num, fact2, fact1);
return (0);
}
