export default function get_list_students_ids(students) {
  if (!Array.isArray(students)) {
    return [];
  }

  return students
    .filter(student => student.id !== undefined)
    .map(student => student.id);
}
