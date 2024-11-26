export default function getStudentByLocation(students, location) {
  return students.filter((student) => student.location === location);
}
