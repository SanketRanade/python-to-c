#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"
double** eigval(double** A);
double** create_ellipse(double a, double b,double** O, int len);
double** line_gen(double** A, double** m);

int main()
{
	//define ellipse parameter
	double F = 9;
	double** V = createMat(2,2);
	V[0][0] = 1/F; V[0][1] = 0;
	V[1][0] = 0; V[1][1] = 3/F;
	double** eig = eigval(V);
	print(eig,2,1);
	double a = 1/sqrt(*eig[0]);
	double b = 1/sqrt(*eig[1]);
	printf("a=%f\n",a);
	printf("b=%f\n",b);
	
	double **center=createMat(2,1);
	*center[0]=0;
	*center[1]=0;
	
	//creating ellipse points
	int len = 1000;
	double**ellipse = create_ellipse(a, b, center, len);
	savetxt(ellipse , "ellipse.dat",2,len);
	
	double **O=createMat(2,2);
	O[0][0]=1, O[1][0]=0;
	O[0][1]=0, O[1][1]=1;
	double **P=createMat(2,1);
	*P[0]=3/sqrt(2);
	*P[1]=sqrt(1.5);
	
	double **m1 = matmul(V,P,2,2,1);
	double **Q=createMat(2,1);
	*Q[0]=-3/sqrt(2);
	*Q[1]=sqrt(1.5);
	
	double **m2=matmul(V,Q,2,2,1);
	
	//generating line points	
	double** x_P = line_gen(P,m1);
	savetxt(x_P,"x_P.dat",2,10);
	double** x_Q = line_gen(Q,m2);
	savetxt(x_Q,"x_Q.dat",2,10);	
	
	return 0 ;
}

double** line_gen(double** A, double** m)
{
	int len = 10;
	double** x_AB = createMat(2,len);
	double** lam = linspace(-12,4,len);
	for (int i=0; i<len; i++)
	{
		x_AB[0][i] = *A[0] + (*lam[i])*(*m[0]);
		x_AB[1][i] = *A[1] + (*lam[i])*(*m[1]);
	}
	return x_AB;
}

double** eigval(double** A)
{
	double** ret = createMat(2,1);
	double a = A[0][0], b = A[0][1];
	double c = A[1][0], d = A[1][1];
	double del = sqrt(((a+d)*(a+d))-4*((a*d)-(b*c)));
	*ret[0] = ((a+d) - del) / 2.0;
	*ret[1] = ((a+d) + del) / 2.0;
	return ret;
}

double** create_ellipse(double a, double b,double** O, int len)  
{
	double** j = createMat(2,len);
	double **theta = linspace(0, 2* M_PI,len);
	for (int i=0;i<len;i++)
	{
		j[0][i] = *O[0] + a*cos(*theta[i]);
		j[1][i] = *O[1] + b*sin(*theta[i]);		
	}
	return j;	
}





