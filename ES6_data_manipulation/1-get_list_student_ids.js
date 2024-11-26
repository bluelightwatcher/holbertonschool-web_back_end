export default function GetListStudentsIds(students) {
  if (!Array.isArray(students)) {
    return [];
  }

  return students
    .filter((student) => student.id !== undefined)
    .map((student) => student.id);
}
