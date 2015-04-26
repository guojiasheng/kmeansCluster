#!/usr/bin/env python
from __future__ import division
import getopt

import sys
import pdb 
import random

import math

class instance:
    attributeValue=[]
    classlable=0

class kmeans:
    iteration=100
    last_cluster=[]
    dataDimesion=2
    cluster=10  
    center=[]    
    centerData=[]    
    dis=[]   
    clusterSample={}   
    dataCluster=[]
    centerData=[]
    def __init__(self,clusterNum,iteration):
        self.cluster=clusterNum
        self.iteration=iteration

    def f2(self,x):
        return x*x
    def f5(self,x):
        return x**0.5
    def add(self,x,y):
        w=[]
        for i in range(0,self.dataDimesion):
            w.append(x[i]+y[i])
    
    def euclideanDistance(self,sampleData,dataCenter):
        self.dis=[]
        for sample in sampleData:
             temp=[]
             for center in dataCenter:
                diff= [x-y for x,y in zip(sample,center)]
                diff=map(self.f2,diff)
                distance=map(self.f5,diff)
                temp.append(distance) 
             self.dis.append(temp)
            
    def initialCenter(self,data):
        instanceNum=len(data)
        if(instanceNum==0):
            print('your input data is empty!')
            return
        for i in range(0,self.cluster):
            index=random.randint(1,instanceNum)
            while (1==1):
               if index in self.center:
                  index=random.randint(1,instanceNum)
               else:
                  self.center.append(index)
                  self.centerData.append(data[index-1])
                  break
              

    def kemeansBulid(self,data):
        self.initialCenter(data)
        self.dataDimesion=len(data[0])
        self.euclideanDistance(data,self.centerData)
        for value in self.dis:
           minIndex=0
           minValue=value[0]
           for i in range(0,len(value)):
               if minValue>=value[i]:
                   minValue=value[i]
                   minIdex=i
           self.dataCluster.append(self.center[minIdex])  
        for j in range(0,len(self.dataCluster)):    
          for i in range(0,len(self.center)):
              if(self.dataCluster[j]==self.center[i]):
                  self.clusterSample.setdefault(self.center[i],[]).append(j)
                  break
        while(self.iteration>0):
            self.iteration=self.iteration-1
            self.bulidCluster(data)
           
            
    def bulidCluster(self,data):
        self.centerData=[]
        self.dataCluster=[]
        for v in self.clusterSample.values():
                x=[]
                for y in v:
                    x.append(data[y])
                element=[]
                for i in range(0,self.dataDimesion):
                    w=0
                    for j in range(0,len(x)):
                        w=w+x[j][i]  
                    element.append(w/len(x))
                self.centerData.append(element)           
        self.euclideanDistance(data,self.centerData)
        self.clusterSample.clear()

        for value in self.dis:
           minIndex=0
           minValue=value[0]
           for i in range(0,len(value)):
               if minValue>=value[i]:
                   minValue=value[i]
                   minIdex=i   
           self.dataCluster.append(self.center[minIdex])      
        for j in range(0,len(self.dataCluster)):    
          for i in range(0,len(self.center)):
              if(self.dataCluster[j]==self.center[i]):
                  self.clusterSample.setdefault(self.center[i],[]).append(j)
                  break
        
    
    def result(self):
        for temp in self.dataCluster:
            for j in range(0,len(self.center)):
                if(temp==self.center[j]):
                     self.last_cluster.append(j)
        myset=set(self.last_cluster)

        print 'Clustered Instances'
        for item in myset:
            print str(item)+'           :'+str(self.last_cluster.count(item))+'('+str(self.last_cluster.count(item)/len(self.last_cluster)*100)[0:2]+"%)"

def Usage():
    print 'kmeans.py usage:'
    print '-h,--help:print help message'
    print '-i: input file'
    print '-n: cluster number'
    print '-t: iteration number'

def main(argv):
     opts, args = getopt.getopt(sys.argv[1:], "hi:n:t:")
     input_file=''
     clusterNum=3
     iteration=10
     for op,value in opts:
         if op in ('-h','--help'):
             Usage()
         elif op == "-i":
             input_file=value
         elif op == "-n":
             clusterNum=value
         elif op== "-t":
             iteration=value
     print input_file
     data=[] 
     f=open(input_file)
     for re in f.readlines():
       a=[]
       temp=re.strip('\n').split(',')
       for x in temp:
         a.append(float(x))
       data.append(a)
     test=kmeans(int(clusterNum),int(iteration))
     test.kemeansBulid(data)
     test.result()
     print 'Instance belong:'
     print test.last_cluster

    
           
if __name__=='__main__':
    main(sys.argv)
               


            
            
        
