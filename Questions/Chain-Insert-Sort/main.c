#include <stdio.h>
#include <stdlib.h> 

typedef struct Point
{
	int data;
	struct Point* next;	
}Point,* pPoint;


pPoint create(int len) 
{

	
	pPoint head,current;
	int i;
	
	head = (pPoint) malloc(sizeof(struct Point));
	current = head;
	head->data = 0; //head �������Ϣ
	 
	if(len == 0)
		return NULL;
	
	for(i=0;i<len;i++)
	{
		current->next = (pPoint) malloc(sizeof(struct Point));
		current = current->next;
		// scanf("%d",&(current->data));
	}
	
	current-> next = NULL;
	return head;
}

void show(pPoint head)
{
	puts("������������:");
    pPoint current=head->next;
    while(current!=NULL)
    {
        printf("data: %d\n",current->data);
        current=current->next;
    }
    puts("=============");
}

//дһ��move�����ƶ�����λ�� 
pPoint move(pPoint p,int len)
{
	int i;
	for(i=0;i<len;i++)
		p = p->	next;
	return p;
}

void swap(pPoint p1,pPoint p2)
{
	int t;
	t = p1->data;
	p1->data = p2->data;
	p2->data = t;
	printf("����: %d,%d    ",p1->data,p2->data);
}
/*
void swapPoint(pPoint p1,pPoint p2)
{
	pPoint t1 = p1->next,t2=p2->next;
	p1->next = p2->next;
	p2->next = t1->next;
	t->next = t2->next;
}
*/
void sort(pPoint head){
	pPoint p = head->next,q,minp;
	for(;p != NULL;p=p->next){
		q = p->next;
		minp = p;
		while(q!=NULL){
			if(q->data <= minp->data){
				minp = q;
			}
			q = q->next; 
		}
		swap(p,minp);
		puts("");
		show(head);
	}
} 

void insert(pPoint head) 
{
	int data;
	pPoint current = head,t,newpoint;
	puts("�����������:");
	scanf("%d",&data);
	newpoint = (pPoint) malloc(sizeof(struct Point));
	newpoint->data = data;

	for(;current != NULL;current = current -> next)
	{
		if(current->next == NULL || data <= current->next->data){
			//printf("��%d֮�����%d",current->data,data);
			t = current->next;
			current->next = newpoint;
			newpoint->next = t;
			break;
		}
	}
	
	puts("�Ѳ���");
	
}

void insert2(pPoint head,pPoint newpoint)
{
	pPoint current = head,t;

	for(;current != NULL;current = current -> next)
	{
		if(current->next == NULL || newpoint -> data <= current->next->data){
			//printf("��%d֮�����%d",current->data,data);
			t = current->next;
			current->next = newpoint;
			newpoint->next = t;
			break;
		}
	}
	
	printf("�Ѳ��� %d\n",newpoint->data);
	
}


void merge(pPoint head1,pPoint head2)
{
	pPoint current = head2->next,t;
	
	while(current != NULL)
	{
		t = current->next;
		insert2(head1,current);
		current = t;
	}

	
}

int main() {
	pPoint head = (pPoint) malloc(sizeof(struct Point));
	head->next = NULL;
	pPoint head2 = (pPoint) malloc(sizeof(struct Point));
	head2->next = NULL;
	
	for(int i=0;i<5;i++)
	{
		insert(head2);
	}
	show(head2);
	getchar();
	
	char input;
	
	puts("�˵�"); 
	puts("s: ��ʾ"); 
	puts("i: ����");
	puts("q: �˳�"); 
	puts("m: ����һ������ϲ�"); 
	
	printf("������:");
	for(input=getchar(); input!='q'; input=getchar())
	{
		switch (input) {
			case 's':
				show(head);
				break;
			case 'i':
				insert(head);
				break;
			case 'm':
				merge(head,head2);
				
		}
		
		getchar(); // ȡ�߻��з� 
		printf("������:");
	}
	
	return 0;
}

