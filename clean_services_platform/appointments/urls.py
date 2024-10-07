from django.urls import path
from . import views

urlpatterns = [
    path('appointments/', views.appointments, name='appointments'),
    # path('appointments/<int:appointment_id>/', views.appointment, name='appointment'),
    # path('appointments/<int:appointment_id>/cancel/', views.cancel_appointment, name='cancel_appointment'),
    # path('appointments/<int:appointment_id>/complete/', views.complete_appointment, name='complete_appointment'),
    # path('appointments/<int:appointment_id>/review/', views.review_appointment, name='review_appointment'),
    # path('appointments/<int:appointment_id>/review/submit/', views.submit_review, name='submit_review'),
    # path('appointments/<int:appointment_id>/review/delete/', views.delete_review, name='delete_review'),
    # path('appointments/<int:appointment_id>/review/edit/', views.edit_review, name='edit_review'),
    # path('appointments/<int:appointment_id>/review/update/', views.update_review, name='update_review'),
    # path('appointments/<int:appointment_id>/review/like/', views.like_review, name='like_review'),
    # path('appointments/<int:appointment_id>/review/unlike/', views.unlike_review, name='unlike_review'),
    # path('appointments/<int:appointment_id>/review/report/', views.report_review, name='report_review'),
    # path('appointments/<int:appointment_id>/review/report/submit/', views.submit_report, name='submit_report'),
    # path('appointments/<int:appointment_id>/review/report/delete/', views.delete_report, name='delete_report'),
    # path('appointments/<int:appointment_id>/review/report/edit/', views.edit_report, name='edit_report'),
    # path('appointments/<int:appointment_id>/review/report/update/', views.update_report, name='update_report'),
    # path('appointments/<int:appointment_id>/review/report/like/', views.like_report, name='like_report'),
    # path('appointments/<int:appointment_id>/review/report/unlike/', views.unlike_report, name='unlike_report'),
    # path('appointments/<int:appointment_id>/review/report/report/', views.report_report, name='report_report'),
    # path('appointments/<int:appointment_id>/review/report/report/submit/', views.submit_report_report, name='submit_report_report'),
]