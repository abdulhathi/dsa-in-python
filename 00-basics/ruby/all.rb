employees = [{
  :name => 'Abdul',
  :age => 45
}, {
  :name => 'Hathi',
  :age => 50
}]

puts employees.any? { |emp| emp[:name] == 'Abdul' }