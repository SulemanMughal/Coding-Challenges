def who_goes_free(n,k):
    return 0 if n==1 else (who_goes_free(n-1, k) + k) % n