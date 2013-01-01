# Problem 1: Find the sum of all integers below 1000 which are divisible by 3 or 5

    li $s0 1000     # limit
    li $s1 1        # counter
    li $s2 3        # 3
    li $s3 5        # 5
    li $t0 0        # total

loop:
    beq $s1, $s0, end   # if counter == 1000, end
    
    div $s1, $s2        # divide counter by 3
    mfhi $t7            # get counter % 3 from hi reg
    beqz $t7, add       # if hi reg == 0, add to total
    
    div $s1, $s3        # divide counter by 4
    mfhi $t7            # get counter % 5 from hi reg
    beqz $t7, add       # if hi reg ==0, add to total
incCounter:
    addi $s1, $s1, 1    # increment counter
    j loop              # continue looping
    
add:
    add $t0, $t0, $s1   # add counter to total
    j incCounter        # jump to increment counter
    
end:
    li $v0, 1           # load print service code
    move $a0, $t0       # load total into arg register
    syscall             # print total

