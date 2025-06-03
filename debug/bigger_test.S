.section .text
.globl _start

_start:
    li t0, 0x10           # t0 = 0x10
    li t1, 0x20           # t1 = 0x20
    add t2, t0, t1        # t2 = 0x30

    # Lưu giá trị t2 vào bộ nhớ
    la t3, test_data
    sw t2, 0(t3)

    # Nạp lại giá trị vào t4
    lw t4, 0(t3)

    # Kiểm thử nhảy điều kiện
    beq t2, t4, equal_label
    li t5, 0xdeadbeef      # Nếu nhảy sai → lỗi
    j end

equal_label:
    li t6, 0xabcdef01

end:
    ebreak                # Dừng tại đây

.section .data
test_data:
    .word 0

