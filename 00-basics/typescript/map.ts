const items = {
  '1': {
    name: 'Abdul',
    id: 1,
    isEligibleToClaim: false,
  },
  '2': {
    name: 'Hathi',
    id: 2,
    isEligibleToClaim: false,
  },
}

Object.values(items).forEach((study) => (study.isEligibleToClaim = true))
console.log(items)
