def balanced_parenthesis(parenthesis)
  st = []
  dic = {'}' => '{', ')' => '(', ']' => '['}
  parenthesis.chars.each do |p|
    if dic.keys.include? p
      return false if (st == [] || dic[p] != st.pop)
    elsif
      st.push(p)
    end
  end
  return st == []
end

puts balanced_parenthesis("([])")
puts balanced_parenthesis('((())')
puts balanced_parenthesis('([)]')
puts balanced_parenthesis('{}([()])')
puts balanced_parenthesis('(()))')