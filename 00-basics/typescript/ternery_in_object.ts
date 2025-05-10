const salary_in_2025 = 10000
const salary_before = 1000
const is_year_2025 = new Date().getFullYear() === 2024
const employee = {
  name: 'Abdul',
  salary: is_year_2025 ? salary_in_2025 : salary_before,
}

console.log(employee)
