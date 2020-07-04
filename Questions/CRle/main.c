/*

说明:
frle 打开文件(dst表示目标,src表示源)，并用rle函数进行压缩。rle函数使用wunit函数写入 行程+数据 单元。
funrle 打开文件，并用unrle函数进行压缩。unrle函数使用wdata函数将 行程+数据 单元 还原为原始数据。
应当使用unsigned char存放数据，因为使用char会导致如果原视数据为0xFF(-1)会错误的判断为EOF

*/

#include <stdio.h>
#include <stdlib.h>

int wunit(FILE* fdst,unsigned char count,unsigned char data){
	//printf("写入: %3u %u \n",count,data);
	 
	fputc(count,fdst);
	fputc(data ,fdst);
	return 0;
}

int rle(FILE* fsrc,FILE* fdst){
	unsigned char count = 0; //行程 
	unsigned char data  = 0;  //数据 
	
	int c = EOF;
	
	while((c=fgetc(fsrc)) != EOF){
		if(c==data && count < 255){
			count++;
		}else{
			wunit(fdst,count,data);
			data  = c;
			count = 1;
		}
	}
	
	wunit(fdst,count,data);
	
	return 0;
}

int wdata(FILE* fdst,unsigned char count,unsigned char data){
	//printf("写入: %3u %c(ASCII: %3d)\n",count,data,data);
	int i;
	for(i=0;i<count;i++){
		fputc(data,fdst);
	}
	return 0;
}

int unrle(FILE* fsrc,FILE* fdst){
	int intcount;
	int intdata;

	while(1){
		intcount = fgetc(fsrc);
		intdata  = fgetc(fsrc);
		if(intcount != -1 && intdata != -1){
			wdata(fdst,(unsigned char)intcount,(unsigned char)intdata);
		}else{
			break;
		}
	}
	return 0;
}

int frle(const char* srcpath,const char* dstpath){
	FILE* fsrc = fopen(srcpath,"rb");
	FILE* fdst = fopen(dstpath,"wb");
	
	// 检查文件是否正常打开 
	if(fsrc == NULL || fdst  == NULL){
		puts("打开文件出错!");
		printf("fsrc == %p\n",fsrc);
		printf("fdst == %p\n",fdst);
		printf("ferror(fsrc) == %d\n",ferror(fsrc)); //若文件流出错则返回非0，否则返回0
		printf("ferror(fdst) == %d\n",ferror(fdst));
		exit(2);
	}
	rle(fsrc,fdst);
	
	fclose(fsrc);
	fclose(fdst);
	return 0;
}

int funrle(const char* srcpath,const char* dstpath){
	FILE* fsrc = fopen(srcpath,"rb");
	FILE* fdst = fopen(dstpath,"wb");
	
	// 检查文件是否正常打开 
	if(fsrc == NULL || fdst  == NULL){
		puts("打开文件出错!");
		printf("fsrc == %p\n",fsrc);
		printf("fdst == %p\n",fdst);
		printf("ferror(fsrc) == %d\n",ferror(fsrc)); //若文件流出错则返回非0，否则返回0
		printf("ferror(fdst) == %d\n",ferror(fdst));
		exit(2);
	}
	
	unrle(fsrc,fdst);
	
	fclose(fsrc);
	fclose(fdst);
	return 0;
}

int main(int argc, char *argv[]) {
	frle("D:\\1\\rle\\apple.bmp","D:\\1\\rle\\apple.rle");
	funrle("D:\\1\\rle\\apple.rle","D:\\1\\rle\\apple_unrle.bmp");
	return 0;
}
