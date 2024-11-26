import getListStudentIds from './1-get_list_student_ids';

export default function getStudentIdsSum(students) {
  const StudentsId = getListStudentIds(students);
  const sum = StudentsId.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
  return sum;
}
