"""Find the binomial coefficent."""
def row(k, i, c):
    """
    match what the function prints.
    >>> row(0, 1, 1)
    1,1,
    """
    if k > i:
        return;
    print( "%d," % c, end="");
    a = c * (i-k)/(k+1);
    return row(k+1, i, a);

def col(i, n):
    """
    match what the function prints.
    >>> col(0, 1)
    1,
    1,1,
    """
    if i > n:
        return;
    row(0, i, 1);
    print("");
    return col(i+1, n);

def main():
    i = 10;
    print( "[INPUT] %d" % i);
    print( "[OUTPUT] ");
    col(0, i);

main()
