      program main
        real(16) :: total = 1
        integer :: i = 1
        print *, huge(total)
        do 
          if (mod(i,2) .EQ. 0) then
            total = total*i
          else
            total = total/i
!            print *, total
          end if
          if (total < 1E-38 .OR. total > 1E38) exit
          i = i+1
        end do
      end program main
