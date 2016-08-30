class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        total = (C-A) * (D - B) + (G-E) * (H - F)
        if A > E:
            A, E = E, A
            C, G = G, C
        width = max(0, min(C, G) - E)
        if B > F:
            B, F = F, B
            D, H = H, D 
        height = max(0, min(D, H) - F)
        return total - width*height