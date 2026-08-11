'''1248.count number of '''
'''def numberOfSubarrays( nums: List[int], k: int) -> int:
    def sub_arr(k):
        if k<0:
            return 0
        left=0
        ans=0
        odd_count=0
        for right in range(len(nums)):
            if nums[right] % 2 !=0:
                odd_count+=1
            while odd_count > k:
                if nums[left]%2!=0:

                    odd_count-=1
                left+=1
            ans+=right-left+1
        
        return ans
    return sub_arr(k)-sub_arr(k-1)
nums=[1,1,2,1,1]
k=3
print(numberOfSubarrays(nums,k))

        '''
def longestNiceSubstring( s: str) -> str:
        if len(s)<2:
            return ""
        unique=set(s)
        for i,ch in enumerate(s):
            if ch.lower() in unique and ch.upper() in unique:
                continue
            l=longestNiceSubstring(s[:i])
            r=longestNiceSubstring(s[i+1:])
            return l if len(l)>=len(r) else r
        return s
s1="YazaAay"
s2="Bb"
s3="c"
print(longestNiceSubstring)
print(longestNiceSubstring)
print(longestNiceSubstring)