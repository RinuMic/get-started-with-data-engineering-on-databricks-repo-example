# Databricks notebook source
def fibonacci(n):
    if n <= 0:
        return "Invalid number!"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        return fib_seq[n-1]
