/*
	DeleteSpace.c for ryosyoku
	author S.KOMATS @ NIT, Kagawa College Takuma

	>>> DeleteSpace *FileName rowNumber
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{

	int i, j, rows;
	char string[1000];
	FILE *fp;


	if ((fp = fopen(argv[1], "r")) == NULL)
	{
		printf("File Open Error.\n");
		return -1;
	}


	rows = atoi(argv[2]);
	for (i = 0; i < rows; i++)
		fgets(string, 1000, fp);


	for (i = 0; i < 1000; i++)
	{
		if (string[i] != ' ')
		{
			for (j = 0; j < 1000; j++)
			{
				if (string[j] == ' ')
				{	
					string[j] = string[i];
					string[i] = ' ';
				}
			}
		}
	}

	printf("%s", string);

	return 0;
}
