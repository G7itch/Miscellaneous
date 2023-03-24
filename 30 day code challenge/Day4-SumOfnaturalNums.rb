num = gets.chomp
num = num.to_i
total = 0
for a in 1..num do
 total = total + a.to_i
end
puts "total = #{total}"