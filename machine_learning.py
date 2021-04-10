import numpy as np
import os
import math

def fibo(n):
	if n <= 2: return 1
	else: return fibo(n - 1) + fibo(n - 2)

