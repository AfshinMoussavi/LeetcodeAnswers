func twoSum(nums []int, target int) []int {
    
    for i, item := range nums{
        complement := target - item
        for j:= i+1; j< len(nums); j++{
            if i != j && nums[j] == complement{
                return []int{i,j}
            }
        }
    }
    return []int{0,0}

}