class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        T=[0]*101   #�έp�Ʀr�X�{���ơA�]�Ʀr1...100�A�}�C�n�}101��
        best = 0    #�̦h���Ʀr�A�X�{�X��?
        for num in nums: #�j��,�w��C�Ӧr���B�z
            T[num]+=1    #�o�ӼƦrnum�X�{����+1
            if T[num]>best:best=T[num]
            #�̦h�X�{T�έp�Ʀr�O�h�� ��o��,T�N���������Ʀr�X�{���Ʀr,�Bbest�N�O�̦h���Ʀr ������̦h���[�_��
        total = 0
        for t in T:#�w��έp���GT�̭����ӼƦrt
            if t==best: total += t
        return total
